
package classeGenerica;

import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;

public class classegenerica {

    public static void main(String[] args) {

        Generica<Integer> g = new Generica<>();
        
//        for (int i = 0; i < 5; i++) {
//            g.add(i);
//        };
        
        g.add(1);
        g.get();
        
        System.out.println("------------------");
        
        List<Integer> lista = new ArrayList<>();
        
        lista.add(1);
        lista.add(2);
        lista.add(3);
        
        for (Integer elemento : lista) { //loop para percorrer todos os elementos de lista
            System.out.println(elemento);
        };
        
        lista.remove(0);
        lista.add(0, 6);
        
        System.out.println("------------------");
        
        Iterator<Integer> iterador = lista.iterator();
        while (iterador.hasNext()) {
            System.out.println(iterador.next());
        };
        
   
    }
    
}
