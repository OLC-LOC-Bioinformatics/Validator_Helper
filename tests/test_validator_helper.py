from validator_helper import validate

column_list = list()
column_list.append(validate.Column('Age', column_type='Range', acceptable_range=2))
column_list.append(validate.Column('Color'))


def test_auto_column_find_everything_good():
    columns = validate.find_all_columns(csv_file='tests/ref_csv.csv',
                                        columns_to_exclude=['Name'])
    validator = validate.Validator(reference_csv='tests/ref_csv.csv',
                                   test_csv='tests/test_all_match.csv',
                                   column_list=columns,
                                   identifying_column='Name')
    assert validator.all_test_columns_in_ref_and_test() is True
    assert validator.same_columns_in_ref_and_test() is True
    assert validator.check_samples_present() is True
    assert validator.check_columns_match() is True


def test_auto_column_find_acceptable_range():
    columns = validate.find_all_columns(csv_file='tests/ref_csv.csv',
                                        columns_to_exclude=['Name'])
    validator = validate.Validator(reference_csv='tests/ref_csv.csv',
                                   test_csv='tests/test_acceptable_range.csv',
                                   column_list=columns,
                                   identifying_column='Name')
    assert validator.all_test_columns_in_ref_and_test() is True
    assert validator.same_columns_in_ref_and_test() is True
    assert validator.check_samples_present() is True
    assert validator.check_columns_match() is True


def test_auto_column_find_outside_range():
    columns = validate.find_all_columns(csv_file='tests/ref_csv.csv',
                                        columns_to_exclude=['Name'])
    validator = validate.Validator(reference_csv='tests/ref_csv.csv',
                                   test_csv='tests/test_outside_range.csv',
                                   column_list=columns,
                                   identifying_column='Name')
    assert validator.all_test_columns_in_ref_and_test() is True
    assert validator.same_columns_in_ref_and_test() is True
    assert validator.check_samples_present() is True
    assert validator.check_columns_match() is False


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


def test_percent_depth_acceptable_range():
    columns = validate.percent_depth_columns(csv_file='tests/ref_genesippr.csv',
                                             columns_to_exclude=['Strain', 'Genus'],
                                             percent_range=2,
                                             depth_range=5)
    validator = validate.Validator(reference_csv='tests/ref_genesippr.csv',
                                   test_csv='tests/test_good_genesippr.csv',
                                   column_list=columns,
                                   identifying_column='Strain')
    assert validator.all_test_columns_in_ref_and_test() is True
    assert validator.same_columns_in_ref_and_test() is True
    assert validator.check_samples_present() is True
    assert validator.check_columns_match() is True


def test_percent_depth_outside_range():
    columns = validate.percent_depth_columns(csv_file='tests/ref_genesippr.csv',
                                             columns_to_exclude=['Strain', 'Genus'],
                                             percent_range=2,
                                             depth_range=5)
    validator = validate.Validator(reference_csv='tests/ref_genesippr.csv',
                                   test_csv='tests/test_bad_genesippr.csv',
                                   column_list=columns,
                                   identifying_column='Strain')
    assert validator.all_test_columns_in_ref_and_test() is True
    assert validator.same_columns_in_ref_and_test() is True
    assert validator.check_samples_present() is True
    assert validator.check_columns_match() is False


def test_resfinder_new_format():
    columns = validate.find_all_columns(csv_file='tests/resfinder_ref.csv',
                                        columns_to_exclude=['Strain'])
    validator = validate.Validator(reference_csv='tests/resfinder_ref.csv',
                                   test_csv='tests/resfinder_good.csv',
                                   column_list=columns,
                                   identifying_column='Strain')
    assert validator.check_resfinderesque_output(one_to_one=True) is True


def test_resfinder_stuff_good():
    columns = validate.find_all_columns(csv_file='tests/resfinder_ref.csv',
                                        columns_to_exclude=['Strain'])
    validator = validate.Validator(reference_csv='tests/resfinder_ref.csv',
                                   test_csv='tests/resfinder_good.csv',
                                   column_list=columns,
                                   identifying_column='Strain')
    assert validator.check_resfinderesque_output()


def test_resfinder_unmatching_categorical():
    columns = validate.find_all_columns(csv_file='tests/resfinder_ref.csv',
                                        columns_to_exclude=['Strain'])
    validator = validate.Validator(reference_csv='tests/resfinder_ref.csv',
                                   test_csv='tests/resfinder_different_categorical.csv',
                                   column_list=columns,
                                   identifying_column='Strain')
    assert validator.check_resfinderesque_output(one_to_one=True) is False


def test_resfinder_outside_range():
    columns = validate.find_all_columns(csv_file='tests/resfinder_ref.csv',
                                        columns_to_exclude=['Strain'])
    validator = validate.Validator(reference_csv='tests/resfinder_ref.csv',
                                   test_csv='tests/resfinder_outside_range.csv',
                                   column_list=columns,
                                   identifying_column='Strain')
    assert validator.check_resfinderesque_output(one_to_one=True) is False


def test_resfinder_missing_sample():
    columns = validate.find_all_columns(csv_file='tests/resfinder_ref.csv',
                                        columns_to_exclude=['Strain'])
    validator = validate.Validator(reference_csv='tests/resfinder_ref.csv',
                                   test_csv='tests/resfinder_missing_sample.csv',
                                   column_list=columns,
                                   identifying_column='Strain')
    assert validator.check_resfinderesque_output(one_to_one=True) is False


def test_resfinder_missing_sample_entry():
    columns = validate.find_all_columns(csv_file='tests/resfinder_ref.csv',
                                        columns_to_exclude=['Strain'])
    validator = validate.Validator(reference_csv='tests/resfinder_ref.csv',
                                   test_csv='tests/resfinder_missing_sample_entry.csv',
                                   column_list=columns,
                                   identifying_column='Strain')
    assert validator.check_resfinderesque_output(one_to_one=True) is False


def test_resfinder_different_allele():
    columns = validate.find_all_columns(csv_file='tests/resfinder_ref.csv',
                                        columns_to_exclude=['Strain'])
    validator = validate.Validator(reference_csv='tests/resfinder_ref.csv',
                                   test_csv='tests/resfinder_different_allele.csv',
                                   column_list=columns,
                                   identifying_column='Strain')
    assert validator.check_resfinderesque_output() is False
