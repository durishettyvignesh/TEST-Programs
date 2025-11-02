import java.io.*;
import java.util.*;

public class javalabprog {
    public static void main(String[] args) {
        try {
            BufferedReader br = new BufferedReader(new FileReader("data.txt"));
            String line;
            List<String[]> rows = new ArrayList<>();

            while ((line = br.readLine()) != null) {
                rows.add(line.split("\\s+")); // split by space or tab
            }
            br.close();

            if (rows.isEmpty()) {
                System.out.println("File is empty.");
                return;
            }

            // find max column widths
            int cols = rows.get(0).length;
            int[] widths = new int[cols];
            for (String[] r : rows) {
                for (int i = 0; i < cols; i++) {
                    if (r[i].length() > widths[i]) widths[i] = r[i].length();
                }
            }

            // print table
            for (String[] r : rows) {
                for (int i = 0; i < cols; i++) {
                    System.out.printf("%-" + (widths[i] + 2) + "s", r[i]);
                }
                System.out.println();
            }

        } catch (Exception e) {
            System.out.println("Error reading file: " + e);
        }
    }
}
