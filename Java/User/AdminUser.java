package User;

public class AdminUser extends BaseUser {
    private String staffId;

    AdminUser (String firstName, String lastName, String staffId) {
        super(firstName, lastName);
        this.staffId = staffId;
    }
}
