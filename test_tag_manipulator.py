from tag_manipulator import TagManipulator

def test_split_empty_string_result_empty_array():
    # arrange
    stringToSplit = ""
    expResult = []
    result = None
    cut = TagManipulator()

    # act
    result = cut.parse_string(stringToSplit)

    # assert
    assert result == expResult

def test_split_comma_empty_string_result_empty_array():
    # arrange
    stringToSplit = ","
    expResult = []
    result = None
    cut = TagManipulator()

    # act
    result = cut.parse_string(stringToSplit)

    # assert
    assert result == expResult

def test_split_one_string_result_array_of_one():
    # arrange
    stringToSplit = "java"
    regex = ","
    expResult = ["java"]
    result = None
    cut = TagManipulator()

    # act
    result = cut.parse_string(stringToSplit, regex)

    # assert
    assert result == expResult

def test_split_one_string_result_array_of_one_whitespace_at_the_beginning():
    # arrange
    stringToSplit = " java"
    regex = ","
    expResult = ["java"]
    result = None
    cut = TagManipulator()

    # act
    result = cut.parse_string(stringToSplit, regex)

    # assert
    assert result == expResult

def test_split_one_string_result_array_of_one_whitespace_at_the_end():
    # arrange
    stringToSplit = "java "
    regex = ","
    expResult = ["java"]
    result = None
    cut = TagManipulator()

    # act
    result = cut.parse_string(stringToSplit, regex)

    # assert
    assert result == expResult

def test_split_one_string_result_array_of_one_coma_at_the_end():
    # arrange
    stringToSplit = "java,"
    regex = ","
    expResult = ["java"]
    result = None
    cut = TagManipulator()

    # act
    result = cut.parse_string(stringToSplit, regex)

    # assert
    assert result == expResult



def test_split_strin_of_two_words_result_array_of_two_strings():
    # arrange
    stringToSplit = "java, python"
    regex = ","
    expResult = ["java", "python"]
    result = None
    cut = TagManipulator()

    # act
    result = cut.parse_string(stringToSplit, regex)

    # assert
    assert result == expResult


def test_split_strin_of_two_phrases_result_array_of_two_strings():
    # arrange
    stringToSplit = "java byte code, python"
    regex = ","
    expResult = ["java byte code", "python"]
    result = None
    cut = TagManipulator()

    # act
    result = cut.parse_string(stringToSplit, regex)

    # assert
    assert result == expResult

def test_split_strin_of_two_phrases_with_witespaces_result_array_of_two_strings():
    # arrange
    stringToSplit = " java byte code , python "
    regex = ","
    expResult = ["java byte code", "python"]
    result = None
    cut = TagManipulator()

    # act
    result = cut.parse_string(stringToSplit, regex)

    # assert
    assert result == expResult