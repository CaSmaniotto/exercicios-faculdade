
/**
 *
 * @author smani
 */
public class ExemploTryCatch {

    public static void main(String args[]) { 
        try {
            String texto = null; 

            String novoTexto = null; 

            novoTexto = texto.toUpperCase(); 

            System.out.println("Texto antigo: "+texto); 

            System.out.println("Texto novo: "+novoTexto); 
        } 
        catch(NullPointerException e) {
            System.out.println("M?todo toUpperCase n?o se aplica a string=null");
        };
  } 
}
