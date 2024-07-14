import java.util.Scanner;
public class SentinelInJava{
public static void main(String [] args){

	Scanner input = new Scanner(System.in);

	int balance = 0 ;
	int withdraw = 0 ;
	int deposit = 0 ;	
	
	System.out.print("Welcome!!!.... Enter your name:");
	String name = input.nextLine();

	System.out.print("How much would you like to withdraw; Enter 1 to deposit and press 2 to withdraw  ");
	int bank = input.nextInt();
	while(bank != -0){


	switch (bank){		
		case 1:
			System.out.println(" Enter amount to deposit again:  ");
			deposit = input.nextInt();
			balance = balance+deposit ;
			System.out.print("Your balance is: "+ balance);

		case 2:
			System.out.print("Enter amount to withdraw:  ");
			withdraw = input.nextInt();
			deposit = input.nextInt();
			if(withdraw <= 0) System.out.print("You are silly!!! Enter correct money.");
			withdraw = balance-withdraw;

			System.out.print("After withdrawer,your balance is:  "+  withdraw);
		default:
			System.out.print("Enter correct number.");
		
}
}
}
}