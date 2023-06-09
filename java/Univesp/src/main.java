import java.util.Scanner;

public class main {

    public static void main(String[] args) {
        
//        Scanner input = new Scanner(System.in);
//        
//        account myAcc = new account();
//        
//        System.out.printf("Initial name is: %s%n%n", myAcc.getName());
//        
//        System.out.println("Please enter the name: ");
//        String _name = input.nextLine();
//        myAcc.setName(_name);
//        System.out.println();
//        
//        System.out.printf("Name in objetc myAcc is: %n%s%n",
//                myAcc.getName());
       String[] vetor = new String[] { "java", "html", "javascript" };

           

            String java = new String("java");

            String html = new String("HTML");

            String javascript = new String("Java");

           

            System.out.print(vetor[0]==java);

            System.out.print(" "+ vetor[1].equalsIgnoreCase(html) + " ");

            System.out.print(vetor[2].startsWith(javascript));
    }
    
}
