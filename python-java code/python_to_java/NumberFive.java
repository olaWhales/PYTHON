import java.util.Scanner;
public class NumberFive{
	public static void main(String...args){

	Scanner input = new Scanner(System.in);

	System.out.println("Enter two integer and i will tell you the relationship they satisfy.");

	System.out.println("Enter first number");
	int number1 = input.nextInt();
	System.out.println("Enter second number");
	int number2 = input.nextInt();

	if(number1 == number2){
			  	System.out.println(number1 + " is equal to " + number2);

	}else if(number1 != number2){
			  	System.out.println(number1 + " not equal to " + number2);

	}if(number1 < number2){
			 	System.out.println(number1 + " is lesser than " + number2);

	}else if(number1 > number2){
				 System.out.println(number1 + " is greater than " + number2);
	
	}if(number1 >= number2){
				 System.out.println(number1 + " is greater and equal to " + number2);

	}else if(number1 <= number2){
				 System.out.println(number1 + " is lesser and equal to " + number2);
	}
	else 
		System.out.println(" not greater and not lesser to any of each ");

		

}


}