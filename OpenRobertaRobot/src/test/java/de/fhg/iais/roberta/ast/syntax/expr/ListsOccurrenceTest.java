package de.fhg.iais.roberta.ast.syntax.expr;

import org.junit.Test;

import de.fhg.iais.roberta.testutil.Helper;

public class ListsOccurrenceTest {
    @Test
    public void Test() throws Exception {
        final String a = "arrayFindFirst({5, 1, 2},2)";

        Helper.assertCodeIsOk(a, "/syntax/lists/lists_occurrence.xml");
    }

    @Test
    public void Test1() throws Exception {
        final String a = "arrayFindLast({5, 1, 2},2)";

        Helper.assertCodeIsOk(a, "/syntax/lists/lists_occurrence1.xml");
    }
}
