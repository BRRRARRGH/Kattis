import java.util.*;
public class Main {
    public static void main(String [] args)
    {
        TreeSet<Character> tree = new TreeSet<Character>();
        Character[] myArray = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 
        'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'};
        tree.addAll(Arrays.asList(myArray));
        Scanner sc = new Scanner(System.in);
        int x = sc.nextInt();
        sc.nextLine();
        for (int i = 0; i < x; i++)
        {
            TreeSet<Character> myTree = (TreeSet<Character>) tree.clone();
            String myString = sc.nextLine().toLowerCase();
            for (int j = 0; j < myString.length(); j++)
            {
                if(myTree.contains(myString[j]))
                {
                    myTree.remove(j);
                }
            }
            if(tree.isEmpty())
            {
                System.out.println("panagram");
            }
            else
            {
                System.out.println("missing " + tree);
            }
        }


    }
}
