import java.io.*;
public class Main {
    public static void main(String[] args) throws IOException
    {
        
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String line = br.readLine();
        while(line != null)
        {
            String[] tokens = line.split(" ");
            System.out.println(Math.abs(Long.parseLong(tokens[0]) - Long.parseLong(tokens[1])));
            line = br.readLine();
        }//While
    }//Main
}//Class
