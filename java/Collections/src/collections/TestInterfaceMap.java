package collections;

import java.util.HashMap;
import java.util.Iterator;
import java.util.Map;
import java.util.Set;

public class TestInterfaceMap {

    public static void main(String[] args) {
        Map<Integer, String> mapNames = new HashMap<Integer, String>();
        mapNames.put(1, "UNIVESP");
        mapNames.put(2, "USP");
        mapNames.put(3, "UNICAMP");
        mapNames.put(3, "UNESP");
        mapNames.put(5, "UFMG");
        System.out.println(mapNames);
        mapNames.remove(2);//removendo o valor referente a chave 2
        
        //resgatando o nome da string referente a chave 2
        System.out.println(mapNames.get(2));
        //retorna os valores do mapNames
        System.out.println(mapNames.values());
        //retorna as chaves
        System.out.println(mapNames.keySet());
        
        Set set = mapNames.entrySet();
        Iterator iterador = set.iterator();
        
        while (iterador.hasNext()) {
            Map.Entry mapentry = (Map.Entry)iterador.next();
            System.out.println("Chave: " + mapentry.getKey());
            System.out.println("Valor " + mapentry.getValue());
        };
    }
    
}
