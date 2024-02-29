package user;

import java.util.Date;
import java.util.UUID;

import subscription.BaseSub;

// a base implemenation of the user of the system
// this class cannot be instantiated
abstract class BaseUser {
    private String id;
    private String authToken;
    private String firstName;
    private String lastName;
    private String middleName;
    private String Email;
    // record the time a new instance is created
    private Date dateCreated;

    BaseUser(String firstName, String lastName,
    String middleName, String Email){
        this.firstName = firstName;
        this.lastName = lastName;
        this.middleName = middleName;
        this.Email = Email;

        this.dateCreated = new Date();
        this.id = UUID.randomUUID().toString();
        this.authToken = UUID.randomUUID().toString();

    }


    public void subscribe(BaseSub sub){
        this.currentSubscription = sub;
    }

    
    // only get the user id, no setter for this
    public String getId() {
        return id;
    }

    // get the user's last name
    public String getLastName() {
        return lastName;
    }

    // set the user's last name
    public void setLastName(String lastName) {
        this.lastName = lastName;
    }

    // get the date the user was created
    public Date getDateCreated() {
        return dateCreated;
    }

    // set the user's first name
    public void setfirstName(String firstName) {
        this.firstName = firstName;
    }  
    
    // get the user's first name
    public String getfirstName() {
        return firstName;
    }

    // acess to the middle name
    public String getMiddleName() {
        return middleName;
    }

    // set the middle name of the user
    public void setMiddleName(String middleName) {
        this.middleName = middleName;
    }

    // give access to the user's email
    public String getEmail() {
        return Email;
    }

    // allow user to set the user email
    public void setEmail(String Email) {
        this.Email = Email;
    }

    // All children must implement this
    abstract void login(String email);

} 