import java.util.Scanner;
public class NumberSix{
	public static void main(String...in){

	Scanner input = new Scanner(System.in);

	
	
		System.out.print("What's your problem ? ");
			String next = input.nextLine();
		System.out.print("Have you had this problem before(yes or no)");
			String option = input.nextLine();
			
				switch (option) {
					case "yes": System.out.print("Well,you have it again");
						break;
					case "no": System.out.print("Well, you have it now");
						break;
					default:
						System.out.print("Enter valid input");

					}
}

}