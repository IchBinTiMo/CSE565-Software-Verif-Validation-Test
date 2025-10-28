import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class VendingMachineTest {

    @Test
    void touch_default_constructor() {
        new VendingMachine(); // covers the implicit no-arg ctor
    }

    // ===== Exact amount (== cost) =====
    @Test
    void candy_exact_cost() {
        String r = VendingMachine.dispenseItem(20, "candy");
        assertEquals("Item dispensed.", r);
    }

    @Test
    void coke_exact_cost() {
        String r = VendingMachine.dispenseItem(25, "coke");
        assertEquals("Item dispensed.", r);
    }

    @Test
    void coffee_exact_cost() {
        String r = VendingMachine.dispenseItem(45, "coffee");
        assertEquals("Item dispensed.", r);
    }

    // ===== More than cost (> cost) =====
    @Test
    void coke_more_than_cost_change_5() {
        String r = VendingMachine.dispenseItem(30, "coke");
        assertEquals("Item dispensed and change of 5 returned", r);
    }

    @Test
    void coffee_more_than_cost_change_5() {
        String r = VendingMachine.dispenseItem(50, "coffee");
        assertEquals("Item dispensed and change of 5 returned", r);
    }

    // ===== Less than cost (< cost) – nested hints =====
    // coffee: input < 45 true, input < 25 false, input < 20 false
    @Test
    void coffee_less_than_cost_purchase_candy_or_coke() {
        String r = VendingMachine.dispenseItem(44, "coffee"); // cost=45, missing 1
        assertEquals("Item not dispensed, missing 1 cents. Can purchase candy or coke.", r);
    }

    // coke: input < 25 true, input < 20 false -> "Can purchase candy."
    @Test
    void coke_less_than_cost_purchase_candy() {
        String r = VendingMachine.dispenseItem(24, "coke"); // cost=25, missing 1
        assertEquals("Item not dispensed, missing 1 cents. Can purchase candy.", r);
    }

    // coke: input < 20 true -> "Cannot purchase item."
    @Test
    void coke_less_than_cost_cannot_purchase() {
        String r = VendingMachine.dispenseItem(19, "coke"); // cost=25, missing 6
        assertEquals("Item not dispensed, missing 6 cents. Cannot purchase item.", r);
    }

    // candy: show overwrite progression; final message must be the strictest
    @Test
    void candy_less_than_cost_cannot_purchase() {
        String r = VendingMachine.dispenseItem(10, "candy"); // cost=20, missing 10
        assertEquals("Item not dispensed, missing 10 cents. Cannot purchase item.", r);
    }

    // ===== Unknown / null item (cost stays 0) =====
    @Test
    void unknown_item_equal_cost_zero() {
        String r = VendingMachine.dispenseItem(0, "tea");
        assertEquals("Item dispensed.", r);
    }

    @Test
    void unknown_item_more_than_cost_zero() {
        String r = VendingMachine.dispenseItem(3, "tea");
        assertEquals("Item dispensed and change of 3 returned", r);
    }

    @Test
    void null_item_equal_cost_zero() {
        String r = VendingMachine.dispenseItem(0, null);
        assertEquals("Item dispensed.", r);
    }
}