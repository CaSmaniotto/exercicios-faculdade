package generica;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;

public class ListaAnimais {
    
    public static void main(String[] args) {
        String[] animais = {"leao", "cobra", "gato", "sapo", "cachorro"};
        List<String> lista = new ArrayList<String>(Arrays.asList(animais));
        
        lista.add("leao");
        lista.add("sapo");
        lista.add("cachorro");
        
        System.out.println("Before");
        for (String item: lista) {
            System.out.println(item);
        };
        
        lista.add(0, "gato");
        System.out.println("Add cat");
        for (String item: lista) {
            System.out.println(item);
        };
        
        System.out.println("Add snake");
        lista.add("cobra");
        for (String item: lista) {
            System.out.println(item);
        };
        
        Collections.sort(lista);
        System.out.println("Sorted array elements: ");
        for (String item: lista) {
            System.out.println(item);
        };
    }
    
}
