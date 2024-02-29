package user;

import Subscription.BaseSub;
import Subscription.SubEnum;

public class Eit extends BaseUser{

    Eit userEit = new Eit("Brighrt", "Ahedor", Email, Email)

    SubEnum duration = SubEnum.FIFTEEN_DAYS;
    BaseSub sub = new Premium(duration, 0);

    userEit.subscribe(sub);

    public Eit(String firstName, String lastName, String middleName, String Email){
        super(firstName, lastName, middleName, Email);
    }

    // the login implementation of the eit user
    @Override
    void login(String Email){
        System.out.println("EIT Logged in");
    }

    
}
