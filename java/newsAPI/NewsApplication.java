import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.Bean;
import org.springframework.web.client.RestTemplate;

@SpringBootApplication
public class NewsApplication {

    public static void main(String[] args) {
        SpringApplication.run(NewsApplication.class, args);
        System.out.println("NewsApplication is running..."); // optional startup message
    }

    // Bean for RestTemplate to make HTTP requests
    @Bean
    public RestTemplate restTemplate() {
        return new RestTemplate();
    }
}
