
import java.io.*;
import java.sql.*;

class jeo1 {
    public static void main (String [] args) throws SQLException {
        Connection conn = DriverManager.getConnection(
                "jdbc:mysql://address=(host=localhost)(port=3306)(user=rich)/jeo",
                "rich", "50915");
        Statement stmt = conn.createStatement();
        ResultSet rs = stmt.executeQuery("select * from users"); 

        rs.first();
        do {
            System.out.print("name: " + rs.getString("name") + ", ");
            System.out.print("id: " + rs.getString("uuid") + ", ");
            System.out.println();
        } while (rs.next());

        return;
    }
}

