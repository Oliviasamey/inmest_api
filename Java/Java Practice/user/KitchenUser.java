package user;

public class KitchenUser extends BaseUser {
    public KitchenUser(String firstName, String lastName, String middleName, String Email){
        super(firstName, lastName, middleName, Email);
    }

    @Override
    void login(String Email){
        System.out.println("Kitchen Staff Logged in");
    }
}
