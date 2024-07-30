public class NumberTwo{
	public static void main(String...args){

	int number = 0 ;
	System.out.printf("%5s%6s%5s%n","Number",	"Square",	"Cube");
	for(int count = 1 ; count <= 5 ; count++){
	System.out.printf("%6d%6d%6d%n",count, count+count , count+count+count);
	}	
}

}