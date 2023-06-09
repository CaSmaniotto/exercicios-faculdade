import java.util.Scanner;

public class main {
    
    public static void main(String[] args) {
       Scanner input = new Scanner(System.in);
       
       Converter conversor = new Converter();
       
       System.out.println("Informe a temperatura: ");
       int temp = input.nextInt();
       conversor.toCelsius(temp);
       conversor.toFar(temp);
       
       conversor.printAll();
       System.out.println();
    }
    
}
