import java.util.Scanner;
public class NumberOne{
	public static void main(String...args){

	System.out.println("Welcome to pass & fail page......");
	Scanner input = new Scanner(System.in);
	
	int number = 11;
	int pass = 0 ;
	int failed = 0 ;
	int userInput = 1;
	
	for(int count = 1 ; count < number ; count++){

	System.out.println("Enter number (1 to passed & 2 to failed)");
	userInput = input.nextInt();

		if(userInput == 1)
			pass = userInput;
			pass = pass+1;
	
		if(userInput == 2)
			failed = userInput;
			failed = failed+1;
		}
	System.out.println("The total number of passed is :  " + pass);
	System.out.println("The total number of failed is :  " + failed);



}

}