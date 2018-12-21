from validator_helper import validate

column_list = list()
column_list.append(validate.Column('Age', column_type='Range', acceptable_range=2))
column_list.append(validate.Column('Color'))


def test_everything_matches():
    validator = validate.Validator(reference_csv='tests/ref_csv.csv',
                                   test_csv='tests/test_all_match.csv',
                                   column_list=column_list,
                                   identifying_column='Name')
    assert validator.all_test_columns_in_ref_and_test() is True
    assert validator.same_columns_in_ref_and_test() is True
    assert validator.check_samples_present() is True
    assert validator.check_columns_match() is True


def test_everything_in_acceptable_range():
    validator = validate.Validator(reference_csv='tests/ref_csv.csv',
                                   test_csv='tests/test_acceptable_range.csv',
                                   column_list=column_list,
                                   identifying_column='Name')
    assert validator.all_test_columns_in_ref_and_test() is True
    assert validator.same_columns_in_ref_and_test() is True
    assert validator.check_samples_present() is True
    assert validator.check_columns_match() is True


def test_outside_acceptable_range():
    validator = validate.Validator(reference_csv='tests/ref_csv.csv',
                                   test_csv='tests/test_outside_range.csv',
                                   column_list=column_list,
                                   identifying_column='Name')
    assert validator.all_test_columns_in_ref_and_test() is True
    assert validator.same_columns_in_ref_and_test() is True
    assert validator.check_samples_present() is True
    assert validator.check_columns_match() is False


def test_testset_has_extra_column():
    validator = validate.Validator(reference_csv='tests/ref_csv.csv',
                                   test_csv='tests/test_add_column.csv',
                                   column_list=column_list,
                                   identifying_column='Name')
    assert validator.all_test_columns_in_ref_and_test() is True
    assert validator.same_columns_in_ref_and_test() is False
    assert validator.check_samples_present() is True
    assert validator.check_columns_match() is True


def test_testset_added_sample():
    validator = validate.Validator(reference_csv='tests/ref_csv.csv',
                                   test_csv='tests/test_add_sample.csv',
                                   column_list=column_list,
                                   identifying_column='Name')
    assert validator.all_test_columns_in_ref_and_test() is True
    assert validator.same_columns_in_ref_and_test() is True
    assert validator.check_samples_present() is False
    assert validator.check_columns_match() is True


def test_differing_categorical():
    validator = validate.Validator(reference_csv='tests/ref_csv.csv',
                                   test_csv='tests/test_differing_categorical.csv',
                                   column_list=column_list,
                                   identifying_column='Name')
    assert validator.all_test_columns_in_ref_and_test() is True
    assert validator.same_columns_in_ref_and_test() is True
    assert validator.check_samples_present() is True
    assert validator.check_columns_match() is False


def test_testset_remove_sample():
    validator = validate.Validator(reference_csv='tests/ref_csv.csv',
                                   test_csv='tests/test_remove_sample.csv',
                                   column_list=column_list,
                                   identifying_column='Name')
    assert validator.all_test_columns_in_ref_and_test() is True
    assert validator.same_columns_in_ref_and_test() is True
    assert validator.check_samples_present() is False
    assert validator.check_columns_match() is True


def test_na_values():
    validator = validate.Validator(reference_csv='tests/ref_csv.csv',
                                   test_csv='tests/test_na_values.csv',
                                   column_list=column_list,
                                   identifying_column='Name')
    assert validator.all_test_columns_in_ref_and_test() is True
    assert validator.same_columns_in_ref_and_test() is True
    assert validator.check_samples_present() is True
    assert validator.check_columns_match() is False


def test_ref_and_test_have_na():
    validator = validate.Validator(reference_csv='tests/test_na_values.csv',
                                   test_csv='tests/test_na_values.csv',
                                   column_list=column_list,
                                   identifying_column='Name')
    assert validator.all_test_columns_in_ref_and_test() is True
    assert validator.same_columns_in_ref_and_test() is True
    assert validator.check_samples_present() is True
    assert validator.check_columns_match() is True
