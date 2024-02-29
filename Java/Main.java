import java.util.Scanner;

import User.AdminUser;

public class Main {
    
    public static void main(String[] args) {
        
        AdminUser adminUser = new AdminUser();
        BaseUser BaseUser = new AdminUser();


        BankAccount brightsAccount =
        new BankAccount(firstName, LastName);
        String number = brightsAccount.getAccountNumber();

        //System.out.println(number);

        //brightsAccount.setAccountNumber(accountNumber:"098089098");
        //brightsAccount.changeValues("Ahedor", "Bright");
        //brightsAccount.changeValues("Ahedor", "Bright", "242434234");

        //System.out.println(brightsAccount.getAccountNumber());//
        
        System.out.println("Program Begins");
        Scanner scanner = new Scanner (System.in);
        String name = scanner.nextLine();
        BankAccount selAccount = new BankAccount(name);

        System.out.println(selAccount.firstName);
    }
}
