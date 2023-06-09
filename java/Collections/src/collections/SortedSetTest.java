package collections;

import java.util.Arrays;
import java.util.SortedSet;
import java.util.TreeSet;

public class SortedSetTest {

    private static final String names[] = { "vermelho", "branco", "azul", 
    "verde", "laranja", "branco", "cinza" };
        // cria um conjunto classificado com TreeSet, e depois o manipula
    
    public SortedSetTest()
    {
        // cria o TreeSet
        SortedSet< String > tree = new TreeSet< String >( Arrays.asList( names ) );
        System.out.println( "sorted set: " );
        printSet( tree ); // gera saída do conteúdo da árvore

        // obtém headSet com base em "laranja"
        System.out.print( "\nheadSet (\"laranja\"): " );
        printSet( tree.headSet( "laranja" ) );

       // obtém tailSet baseado em "laranka"
        System.out.print( "tailSet (\"laranja\"): " );
        printSet( tree.tailSet( "laranja" ) );
        // obtém primeiro e últimos elementos
        System.out.printf( "first: %s\n", tree.first() );
        System.out.printf( "last : %s\n", tree.last() );
    } // fim do construtor SortedSetTest

    // gera saída do conteúdo
    private void printSet( SortedSet< String > set )
    {
        for ( String s : set )
        System.out.printf( "%s ", s ); 
        System.out.println();
    } // fim do método printSet
    
    public static void main( String args[] )
    {
        new SortedSetTest();
    } // fim do main
} // fim da classe SortedSetTest

