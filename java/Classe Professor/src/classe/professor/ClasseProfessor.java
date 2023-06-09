
package classe.professor;


public class ClasseProfessor {


    public static void main(String[] args) {
        
//        System.out.println("Professor P1: \n");
//        Professor p1 = new Professor("Ronaldo", "123");
//        System.out.println("Matricula: " + p1.getMatricula());
//        System.out.println("Nome: " + p1.getNome());
//        System.out.printf("Salario: %.2f",p1.calcSalario(20, 70));
        
        System.out.println("\n Professor Concursado P2: \n");
        ProfessorConcursado p2 = new ProfessorConcursado("Cris", "555");
        System.out.println("Matricula: " + p2.getMatricula());
        System.out.println("Nome: " + p2.getNome());
        System.out.printf("Salario: %.2f",p2.calcSalario(20, 70));
        
        System.out.println("\n \n Professor Horista P3: \n"); 
        ProfessorConcursado p3 = new ProfessorConcursado("Ana", "564");
        System.out.println("Matricula: " + p3.getMatricula());
        System.out.println("Nome: " + p3.getNome());
        System.out.printf("Salario: %.2f", p3.calcSalario(40, 5.03));
        
    }
    
}
