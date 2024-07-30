import java.util.Scanner;
public class NumberEleven{
	public static void main(String...args){

	Scanner input = new Scanner(System.in);

	double gallon = 0 ;
	double miles = 0 ;
	double totalMileDriving = 0 ;
	double totalGallonUsed = 0 ;
	double totalMilesPerGallon = 0 ;

	while(miles != -50){
		System.out.print("Enter the numbers of gallon used to end (PRESS -50 TO END) :" );
		gallon = input.nextDouble();
		totalGallonUsed = totalGallonUsed + gallon ;

		System.out.print("Enter the numbers of miles driving: ");
		miles = input.nextDouble();
		totalMileDriving = totalMileDriving + miles ; 
		
		
		totalMilesPerGallon = totalMileDriving / totalGallonUsed ;
		System.out.println("Total is: " + totalMilesPerGallon);

	}	
		System.out.print("The overall total Miles Per Gallon used is : " + totalMilesPerGallon );

}

}