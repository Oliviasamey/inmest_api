public class BankAccount {
    public String firstName;
    private String lastName;
    private String middleName;
    private String accountNumber;

    BankAccount(String firstName, String lastName, String middleName, String accountNumber) {
        this.accountNumber = accountNumber;
        this.firstName = firstName;
        this.lastName = lastName;
        this.middleName = middleName;
    }

    BankAccount(String firstName, String lastName, String middleName) {
        this.firstName = firstName;
        this.lastName = lastName;
        this.middleName = middleName;
    }

        BankAccount(String firstName) {
        this.firstName = firstName;
    }

    /*
     * function to change the names
     * @param lastName, the account lastname
     * @param middleName,
     */


    public void changeValues(String lastName, String middleName){
        this.lastName = lastName;
        this.middleName = middleName;
    }

    public void changeValues(String lastName, String middleName, String accountNumber){
        this.lastName = lastName;
        this.middleName = middleName;
        this.accountNumber = accountNumber;
    }

    public void setLastName(String lastName) {
        this.lastName = lastName;
    }

    public void setAccountNumber(String accountNumber) {
        if (accountNumber.length() !=10) {
            return;          
        }
        this.accountNumber = accountNumber;
    }

    public String getFirstName() {
        return firstName;
    }

    public String getAccountNumber() {
        return accountNumber;
    }

    public String getLastName() {
        return lastName;
    }

    public String getMiddleName() {
        return middleName;
    }
}
