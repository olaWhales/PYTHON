import java.util.Scanner;
public class NumberEight{
public static void main(String...arg){

	Scanner input = new Scanner(System.in);


	int lowest = 0;
	int largest = 0;
	int sum = 0 ;
	for(int count = 0 ; count < 10 ; count++){
	System.out.print("Enter number one - ten: ");
	int number = input.nextInt();

		sum = sum + number ;
		sum++
		
		if(number > largest)
			largest = number;
		if(lowest == 0 || lowest > number)
			lowest = number;

	}
	System.out.println("the largest number is: " + largest);
	System.out.println("the lowest number is : " + lowest);
	System.out.print("The sum of all numbers is " + sum)
}

}