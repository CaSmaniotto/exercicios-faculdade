public class Converter {
    private float celsius;
    private float fahrenheits;
    
    public Converter() {};
    
    public void toCelsius(int temperatura) 
    {
       this.celsius = (float) ((temperatura - 32) / 1.8);
    };
    
    public void toFar(int temperatura) 
    {
        this.fahrenheits = (float) ((temperatura * 1.8) + 32);
    };
    
    public void printAll() 
    {
        System.out.printf("Valor em fahrenheits: %n" + fahrenheits);
        System.out.println();
        System.out.printf("Valor em celsius: %n" + celsius);
    }
}
