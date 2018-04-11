from datetime import datetime


def test_constructed_stock_with_correct_date_added_to_database(db_session):
    from ..models import Entry

    assert len(db_session.query(Stock).all()) == 0
    stock = Stock(
        symbol='WTF',
        companyName='Wha The Foo',
        CEO='Him',
        website='www.foobar.com',
        industry='yup',
        sector='9th',
        exchange='NYSE',
        issueType='cs',
        description='Does WTF he likes, when he likes'
    )
    db_session.add(stock)
    assert len(db_session.query(Stock).all()) == 1


def test_constructed_stock_with_no_date_added_to_database(db_session):
    from ..models import Stock

    assert len(db_session.query(Stock).all()) == 0
    stock = Stock(
        symbol='f',
        companyName='Ford Motor Company'
    )
    db_session.add(stock)
    assert len(db_session.query(Stock).all()) == 1


# def test_constructed_stock_with_date_added_to_database(db_session):
#     from ..models import Stock

#     assert len(db_session.query(Stock).all()) == 0
#     stock = Stock(
#         title='test 1',
#         body='this is a test',
#         date=datetime(2017, 10, 12, 1, 30)
#     )
#     db_session.add(entry)
#     assert len(db_session.query(Entry).all()) == 1


def test_stock_with_no_symbol_throws_error(db_session):
    from ..models import Stock
    import pytest
    from sqlalchemy.exc import IntegrityError

    assert len(db_session.query(Stock).all()) == 0
    stock = Stock(
        symbol='f',
        companyName='Ford Motor Company'
    )
    with pytest.raises(IntegrityError):
        db_session.add(stock)

        assert db_session.query(Stock).one_or_none() is None