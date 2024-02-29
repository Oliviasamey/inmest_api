public class User{
    //first name of the user
    String firstName = "SAMEY";
    String lastName = "Olivia";
    int age = 0;
    boolean hasMoney = true;

    public static void main(String[] args) {
        double amountPaid = 23.05;
        double amountCredited = 12;
        double result = amountPaid/amountCredited;
        
        int amountConverted = (int) amountPaid;
        System.out.println("New Value:" + amountConverted);
        System.out.println("Result:" + result);
    }
    
}