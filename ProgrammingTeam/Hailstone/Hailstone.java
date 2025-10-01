import java.util.*;
public class Hailstone {
    private static long sum = 0;
    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);
        long num = sc.nextLong();
        hailstone(num);
        System.out.println(sum);

    }
    public static void hailstone(long num)
    {
        sum+= num;
        if(num != 1)
        {
            if (num % 2 == 0)
            {
                hailstone(num / 2);
            }
            else
            {
                hailstone((3 * num) + 1);
            }
        }

    }

}
