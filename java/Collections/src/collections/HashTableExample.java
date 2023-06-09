package collections;

import java.util.Enumeration;
import java.util.Hashtable;

public class HashTableExample {
    public static void main(String[] args) {
        Enumeration names;
        String key;
        // Cria a tabela hash
        Hashtable<String, String> hashtable = new Hashtable<String, String>();
        // Adiciona o par chave/valor
        hashtable.put("Chave1","UNIVESP");
        hashtable.put("Chave2","USP");
        hashtable.put("Chave3","UNICAMP");
        hashtable.put("Chave4","UNESP");
        hashtable.put("Chave0","Mona");
        names = hashtable.keys();
        while(names.hasMoreElements()) {
            key = (String) names.nextElement();
            System.out.println("Chave: " +key+ " & Valor: " + hashtable.get(key));
        }
    }
}
