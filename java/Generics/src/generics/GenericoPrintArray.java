package generics;

public class GenericoPrintArray {

    public static <E> void printArray(E[] inputArray){
        
        for (E element: inputArray) 
            System.out.printf("%s ", element);
        
        System.out.println("");
    };
    
    public static void main(String[] args) {

        Double[] doubleArray = {1.1, 2.2, 3.3, 4.4, 5.1};
        Integer[] integerArray = {1, 2, 3, 4, 5, 6};
        Character[] charArray = {'C', 'A', 'E', 'T', 'A', 'N', 'O'};
        
        System.out.println("Double Array: ");
        printArray(doubleArray);
        System.out.println("Integer Array: ");
        printArray(integerArray);
        System.out.println("Character Array: ");
        printArray(charArray);
        
    }
    
}
