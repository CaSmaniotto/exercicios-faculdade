
package classe.professor;

public class ProfessorHorista extends Professor{
    public ProfessorHorista(String nome, String matricula) {
        super(nome, matricula);
    }
    
    @Override
    public double calcSalario(int hora, double valor_hora) {
        return hora * valor_hora;
    }
}
