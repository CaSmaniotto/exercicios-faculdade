
package testes;


public class SubClasse extends SuperClasse {
    public void imprimeMetodo() {
        super.imprimeMetodo() ;
        System.out.println("Impresso na SUBCLASSE");
    }

    @Override
    public void buu(){
        System.out.println("uub");
    };
}    