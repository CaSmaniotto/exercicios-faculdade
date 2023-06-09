package generica;

import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

public class ListaAnimais2 {

    public static void main(String[] args) {
        
        List<Animal> lista = new ArrayList<Animal>();
        lista.add(new Animal("peixe", "azul", "raro"));
        lista.add(new Animal("mico", "dourado", "raro"));
        lista.add(new Animal("vaca", "preta", "comum"));
        lista.add(new Animal("porco", "rosa", "comum"));
        
        for (Animal obj: lista) {
            System.out.println(obj.get());
        };
    }
}
