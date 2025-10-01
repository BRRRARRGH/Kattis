import java.util.*;

public class Main {
    public static void main(String[] args) {
        HashMap<Character, Character> myHash = new HashMap<>();
        Scanner sc = new Scanner(System.in);
        myHash.put('1', '`');
        myHash.put('2','1');
        myHash.put('3','2');
        myHash.put('4','3');
        myHash.put('5','4');
        myHash.put('6','5');
        myHash.put('7','6');
        myHash.put('8','7');
        myHash.put('9','8');
        myHash.put('0','9');
        myHash.put('-','0');
        myHash.put('=','-');
        myHash.put('w','q');
        myHash.put('e','w');
        myHash.put('r','e');
        myHash.put('t','r');
        myHash.put('y','t');
        myHash.put('u','y');
        myHash.put('i','u');
        myHash.put('o','i');
        myHash.put('p','o');
        myHash.put('[','p');
        myHash.put(']','[');
        myHash.put('\\',']');
        myHash.put('s','a');
        myHash.put('d','s');
        myHash.put('f','d');
        myHash.put('g','f');
        myHash.put('h','g');
        myHash.put('j','h');
        myHash.put('k','j');
        myHash.put('l','k');
        myHash.put(';','l');
        myHash.put('\'',';');
        myHash.put('x','z');
        myHash.put('c','x');
        myHash.put('v','c');
        myHash.put('b','v');
        myHash.put('n','b');
        myHash.put('m','n');
        myHash.put(',','m');
        myHash.put('.',',');
        myHash.put('/','.');
        myHash.put(' ', ' ');
        while(sc.hasNextLine())
        {
            String myGuy = sc.nextLine().toLowerCase();
            String myBetterGuy = "";
            for (int i = 0; i < myGuy.length(); i++)
            {
                myBetterGuy += myHash.get(myGuy.charAt(i));
            }
            System.out.println(myBetterGuy.toUpperCase());
        }
        
    }
}
