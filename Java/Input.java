import java.util.Scanner;
class Input {
	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		System.out.print("Wpisz coś: ");
		String input = in.nextLine();
		System.out.println("Wpisałeś " + input + ".");
	}	
}