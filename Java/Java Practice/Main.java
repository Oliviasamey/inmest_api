import Subscription.BaseSub;
import Subscription.FreemiumSub;
import Subscription.SubEnum;
import user.Eit;

public class Main {
    public static void main(String[] args) {
        BaseSub freemiumSub = new FreemiumSub(SubEnum.FIFTEEN_DAYS, 0);

        Eit userEit = 
        new Eit("Bright", "Ahedor", "Kwame", "bright@gmail.com");
        userEit.login("email");
    }
    
}
