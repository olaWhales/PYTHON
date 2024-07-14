import java.util.Scanner;
public class NumberEleven{
	public static void main(String...args){

	Scanner input = new Scanner();

	int gallon = 0 ;
	int miles = 0 ;
	int totalMileDriving = 0 ;
	int totalGallonUsed = 0 ;
	int totalMilesPerGallon = 0 ;
	
	System.out.print("Enter the numbers of miles driving: ");
	gallon = input.nextInt();
	System.out.print("Enter the numbers of gallon used: ");
	miles = input.nextInt();

	while(miles != -50){
		System.out.print("Enter the numbers of miles driving: (-50 to end)");
		gallon = input.nextInt();
		totalGallonUsed = totalGallonUsed + gallon ;

		System.out.print("Enter the numbers of gallon used: ");
		miles = input.nextInt();
		totalMileDriving = totalMileDriving + miles ; 
		
		totalMilesPerGallon = totalMileDriving / totalGallonUsed ;
	}	
		System.out.print("The total Miles Per Gallon used is : " + totalMilesPerGallon );

}

}