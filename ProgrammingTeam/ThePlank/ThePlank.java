import java.util.*;
class ThePlank
{
    static int checkLength(int length)
    {
        if(length < 0)
        {
            return 0;
        }
        else if(length == 0)
        {
            return 1;
        }
        else 
        {
            int sum = 0;
            for(int i = 1; i < 4; i++)
            {
                sum += checkLength(length - i);
            }
            return sum;
        }
        
    }
    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);
        int numMeter = sc.nextInt();
        System.out.println(checkLength(numMeter));
        
    }
}