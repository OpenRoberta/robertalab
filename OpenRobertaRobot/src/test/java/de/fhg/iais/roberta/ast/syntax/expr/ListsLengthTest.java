package de.fhg.iais.roberta.ast.syntax.expr;

import org.junit.Test;

import de.fhg.iais.roberta.testutil.Helper;

public class ListsLengthTest {
    @Test
    public void Test() throws Exception {
        final String a = "ArrayLen({(0.1),(0.0),0})";

        Helper.assertCodeIsOk(a, "/syntax/lists/lists_length.xml");
    }
}
