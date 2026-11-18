---
title: "Spring Boot ile entegrasyon testi yazımı"
date: 2022-02-03
description: "H2 gömülü veritabanı ve JUnit 4 ile bir servis ile repository arasındaki entegrasyonu test etmek."
tags: ["spring-boot", "test", "java"]
---

## Entegrasyon testi nedir?

Yazılımın parçaları arasındaki entegrasyonun test edilmesi amacıyla yazılan test senaryoları bütününe entegrasyon testi denir. Uzun yılların birikimiyle oluşan yazılım geliştirme prensipleri her sınıfın tek bir amaca hizmet etmesini öğütler. Böyle bir senaryoda uygulamalar büyük çoğunlukla tek bir bileşenden oluşmaz, birden çok sınıfın bir araya gelmesiyle oluşmuş yapılardır. Bu parçaların her birini birbirinden bağımsız özellikler olarak test etme yöntemine birim test denir.

Başarılı çalışan entegrasyon testleri, parçaların birbiriyle doğru şekilde entegre çalıştığını gösterir. Birim ve entegrasyon testlerinin yazım sırası konusundaki tartışmayı daha iyi kavramak için Software Engineering Stack Exchange'teki [When should I write integration tests?](https://softwareengineering.stackexchange.com/search?q=%22When+should+I+write+integration+tests%22) sorusuna göz atabilirsiniz.

Bu yazıda veritabanına basit CRUD işlemleriyle veri kaydeden bir mikroservis örneği üzerinden ilerleyeceğiz. Bu örnekte Hibernate kullanılarak oluşturulmuş bir repository ve işlemlerin gerçekleştirildiği servis katmanı bulunuyor.

### Servis katmanı

```java
@Service
public class UserServiceImpl implements UserService {

    private final UserRepository userRepository;

    @Autowired
    public UserServiceImpl(UserRepository userRepository) {
        this.userRepository = userRepository;
    }

    @Override
    public ManipulationResponse createUser(CreateUserRequest request) throws CustomException {
        UserDto createUserDto = new UserDto();
        if (userRepository.findByMail(request.getMail()).isPresent()) {
            throw new BusinessException(USER_ALREADY_EXIST);
        }
        createUserDto.setFirstName(request.getFirstName());
        createUserDto.setSurName(request.getSurName());
        createUserDto.setMail(request.getMail());

        userRepository.save(createUserDto);
        return ManipulationResponse.SUCCESS_PROCESS;
    }

    @Override
    public UserDto getUser(String mail) throws CustomException {
        Optional<UserDto> user = userRepository.findByMail(mail);
        if (user.isEmpty()) {
            throw new DataNotFoundException(USER_NOT_FOUND);
        }
        return user.get();
    }
}
```

### Repository katmanı

```java
public interface UserRepository extends JpaRepository<UserDto, Long> {

    Optional<UserDto> findByMail(String mail);

}
```

### Data Transfer Object

```java
@Entity(name = "user")
public class UserDto {
    @Id
    @GenericGenerator(name = "uuid", strategy = "uuid2")
    @GeneratedValue(generator = "uuid")
    @Column(name = "user_id")
    private String userId;
    @Column(name = "first_name")
    private String firstName;
    @Column(name = "surname")
    private String surName;
    @Column(name = "mail")
    private String mail;
}
```

Bu örnekte repository ile servisin entegrasyonunu test edeceğiz. İşlemlerin gerçekleştirileceği katmanları ve objenin yapısını gösterdiğimize göre entegrasyon testinin yazılması aşamasına geçebiliriz.

## Bağımlılıkların eklenmesi

İlk aşama gerekli bağımlılıkların eklenmesi. Aşağıdaki bağımlılıkları projenin `pom.xml` dosyasına ekliyoruz. Testler için JUnit 4, veritabanı olarak da H2 gömülü veritabanını kullanacağız.

```xml
<dependency>
    <groupId>com.h2database</groupId>
    <artifactId>h2</artifactId>
    <scope>test</scope>
</dependency>
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-test</artifactId>
    <scope>test</scope>
    <exclusions>
        <exclusion>
            <groupId>org.junit.vintage</groupId>
            <artifactId>junit-vintage-engine</artifactId>
        </exclusion>
    </exclusions>
</dependency>
<dependency>
    <groupId>org.junit.vintage</groupId>
    <artifactId>junit-vintage-engine</artifactId>
    <scope>test</scope>
    <exclusions>
        <exclusion>
            <groupId>org.hamcrest</groupId>
            <artifactId>hamcrest-core</artifactId>
        </exclusion>
    </exclusions>
</dependency>
```

## Test profili

Projemizin `src/test/resources` klasörünün altına `application-test.yml` dosyası oluşturuyoruz. Bu klasör yoksa kendimiz oluşturabiliriz. Dosya `application-test.properties` biçiminde de olabilir; hangi dosya tipinin kullanıldığı fark etmez, yalnızca yazım biçimi değişir. İkinci biçimi kullanıyorsanız aşağıdaki içeriği `.properties` biçimine göre yeniden düzenlemeniz gerekir. Oluşturduğumuz dosyaya şu içeriği yerleştiriyoruz:

```yaml
spring:
  application:
    name: $PROJECT_NAME
  jpa:
    database: h2
    show-sql: true
    generate-ddl: true
    hibernate:
      ddl-auto: create-drop
  cache:
    type: none
  datasource:
    url: jdbc:h2:mem:link;DB_CLOSE_DELAY=-1;DB_CLOSE_ON_EXIT=FALSE
    username: $USERNAME
    password: $PASSWORD
    driver-class-name: org.h2.Driver
  sql:
    init:
      mode: always
```

## Test sınıfı

Test için veritabanı bağlantısı hazır olduğuna göre entegrasyon testi için bir sınıf oluşturabiliriz. `UserServiceImpl` sınıfı için bir entegrasyon testi yazacağımdan adını `UserServiceImplIntegrationTest` koyuyorum. Testini yazacağımız sınıfla aynı paket yapısında, test klasörü altında yeni bir sınıf oluşturuyoruz:

```text
src
├── main
│   └── java/.../service/UserServiceImpl.java
└── test
    ├── java/.../service/UserServiceImplIntegrationTest.java
    └── resources/application-test.yml
```

Bu aşamada entegrasyon testini yazmaya başlayabiliriz. İlk olarak sınıfa gerekli anotasyonları ekliyoruz:

- `@SpringBootTest`: Testlerde kullanılmak üzere bir `ApplicationContext` oluşturulmasını sağlar.
- `@ActiveProfiles("test")`: Sınıftaki testlerin `test` profilini, yani `application-test.yml` dosyasını kullanmasını sağlar.
- `@RunWith(SpringJUnit4ClassRunner.class)`: Sınıfın, Spring'in JUnit 4 desteğiyle çalışması gerektiğini belirtir.

Bu anotasyonlarla sınıfı oluşturuyoruz. Servis için birim test yazıyor olsaydık repository sınıfını mock'lamamız gerekecekti. Ancak entegrasyon testlerinde iki öğenin birbiriyle ilişkisini test ettiğimiz için her iki sınıfın da gerçek fonksiyonlarına ihtiyacımız var. Bu sebeple repository'yi Spring'den alıp servisi onunla oluşturuyoruz.

```java
@SpringBootTest
@ActiveProfiles("test")
@RunWith(SpringJUnit4ClassRunner.class)
public class UserServiceImplIntegrationTest {

    @Autowired
    private UserRepository repository;

    private UserServiceImpl service;

    @Before
    public void init() {
        service = new UserServiceImpl(repository);
    }
}
```

Artık testlerimizi ekleyebiliriz. Ben yeni bir kullanıcının oluşturulduğu durum için bir test yazdım. Bu testte önce kullanıcı H2 veritabanına ekleniyor, sonra eklenen veri çekilerek servis isteğindeki verilerle karşılaştırılıyor.

```java
@SpringBootTest
@ActiveProfiles("test")
@RunWith(SpringJUnit4ClassRunner.class)
public class UserServiceImplIntegrationTest {

    @Autowired
    private UserRepository repository;

    private UserServiceImpl service;

    @Before
    public void init() {
        service = new UserServiceImpl(repository);
    }

    @Test
    public void createUser_whenSuccess() throws CustomException {
        ManipulationResponse result = service.createUser(Helper.getCreateUserRequest());

        Optional<UserDto> dbData = repository.findByMail("abc@def.com");

        // We are controlling results for being null or not
        assertNotNull(result);

        // Then we control the process is completed successfully
        assertEquals(ManipulationResponse.SUCCESS_PROCESS, result);

        // Lastly, we check the some fields of Dto
        assertEquals(dbData.orElseThrow().getFirstName(), Helper.getCreateUserRequest().getFirstName());
    }
}
```

## Önemli notlar

Spring Security kullanıyorsanız bu kütüphane bazen entegrasyon testlerinin çalışmasına engel olabiliyor. Çözüm yolları için Stack Overflow'daki [Disable security for unit tests with spring boot](https://stackoverflow.com/questions/23894010) sorusuna bakabilirsiniz.

Entegrasyon testleri bittikten sonra test veritabanındaki verileri silmeyi unutmayın. `application-test.yml` dosyamızda bunun için zaten bir ayar var, ancak verilerin çakışmaması için ayrıca dikkat etmek gerekir:

```yaml
spring:
  jpa:
    hibernate:
      ddl-auto: create-drop
```

Test verilerinin eklendiği H2 bağımlılığının `scope` değerinin `test` olduğundan emin olun.

`application-test.yml` dosyasını koyacağımız `src/test` altında `resources` klasörü yoksa ve onu kendimiz oluşturduysak, IDE bazen bu klasörün test kaynaklarının bulunduğu klasör olduğunu anlayamıyor. Kullandığınız IDE'de bu klasörü test kaynak klasörü olarak işaretlemek sorunu çözer.

---

*Bu yazı ilk olarak 3 Şubat 2022'de [Medium'da](https://medium.com/@gulolkenan/spring-boot-ile-entegrasyon-testi-yaz%C4%B1m%C4%B1-21a36ea650c7) yayımlandı.*
