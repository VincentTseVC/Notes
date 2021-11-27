"""CSC108/A08: Fall 2021 -- Assignment 3: arxiv.org

This code is provided solely for the personal and private use of
students taking the CSC108/CSCA08 course at the University of
Toronto. Copying for purposes other than this use is expressly
prohibited. All forms of distribution of this code, whether as given
or with any changes, are expressly prohibited.

All of the files in this directory and all subdirectories are:
Copyright (c) 2021 Anya Tafliovich.

"""

import copy  # needed in examples of functions that modify input dict
from typing import Dict, List, TextIO

# remove unused constants from this import statement when you are
# finished your assignment
from constants import (ID, TITLE, CREATED, MODIFIED, AUTHORS,
                       ABSTRACT, END, SEPARATOR, NameType,
                       ArticleValueType, ArticleType, ArxivType)


EXAMPLE_ARXIV = {
    '008': {
        'identifier': '008',
        'title': 'Intro to CS is the best course ever',
        'created': '2021-09-01',
        'modified': None,
        'authors': [('Ponce', 'Marcelo'), ('Tafliovich', 'Anya Y.')],
        'abstract': '''We present clear evidence that Introduction to
Computer Science is the best course.'''},
    '031': {
        'identifier': '031',
        'title': 'Calculus is the best course ever',
        'created': None,
        'modified': '2021-09-02',
        'authors': [('Breuss', 'Nataliya')],
        'abstract': '''We discuss the reasons why Calculus I
is the best course.'''},
    '067': {'identifier': '067',
            'title': 'Discrete Mathematics is the best course ever',
            'created': '2021-09-02',
            'modified': '2021-10-01',
            'authors': [('Bretscher', 'Anna'), ('Pancer', 'Richard')],
            'abstract': ('We explain why Discrete Mathematics is the best ' +
                         'course of all times.')},
    '827': {
        'identifier': '827',
        'title': 'University of Toronto is the best university',
        'created': '2021-08-20',
        'modified': '2021-10-02',
        'authors': [('Bretscher', 'Anna'),
                    ('Ponce', 'Marcelo'),
                    ('Tafliovich', 'Anya Y.')],
        'abstract': '''We show a formal proof that the University of
Toronto is the best university.'''},
    '042': {
        'identifier': '042',
        'title': None,
        'created': '2021-05-04',
        'modified': '2021-05-05',
        'authors': [],
        'abstract': '''This is a very strange article with no title
and no authors.'''}
}

EXAMPLE_BY_AUTHOR = {
    ('Ponce', 'Marcelo'): ['008', '827'],
    ('Tafliovich', 'Anya Y.'): ['008', '827'],
    ('Bretscher', 'Anna'): ['067', '827'],
    ('Breuss', 'Nataliya'): ['031'],
    ('Pancer', 'Richard'): ['067']
}


# We provide this PARTIAL docstring to show the use of examples.
def make_author_to_articles(id_to_article: ArxivType) -> Dict[NameType,
                                                              List[str]]:
    """Return a dict that maps each author name to a list (sorted in
    lexicographic order) of IDs of articles written by that author,
    based on the information in id_to_article.

    >>> make_author_to_articles(EXAMPLE_ARXIV) == EXAMPLE_BY_AUTHOR
    True

    """
    author_to_articles = {}
    for _id in id_to_article:
        for author in id_to_article[_id][AUTHORS]:
            
            if author not in author_to_articles:
                author_to_articles[author] = []
            author_to_articles[author].append(_id)
    return author_to_articles


def get_coauthors(id_to_article: ArxivType, author: NameType) -> List[NameType]:
    """
    >>> get_coauthors(EXAMPLE_ARXIV, ('Tafliovich', 'Anya Y.'))
    [('Bretscher', 'Anna'), ('Ponce', 'Marcelo')]
    """
    coauthors = []
    # author_to_articles = make_author_to_articles(id_to_article)
    # for _id in author_to_articles[author]:
    for _id in id_to_article:
        if author in id_to_article[_id][AUTHORS]:
            for coauthor in id_to_article[_id][AUTHORS]:
                if coauthor not in coauthors and coauthor != author:
                    coauthors.append(coauthor)
    coauthors.sort()
    return coauthors


def get_most_published_authors(id_to_article: ArxivType) -> List[NameType]:
    """
    >>> get_most_published_authors(EXAMPLE_ARXIV)
    [('Bretscher', 'Anna'), ('Ponce', 'Marcelo'), ('Tafliovich', 'Anya Y.')]
    """
    author_to_articles = make_author_to_articles(id_to_article)
    authors = []
    max_articles = 0
    for author in author_to_articles:
        num_articles = len(author_to_articles[author])
        if num_articles > max_articles:
            max_articles = num_articles
            authors = [author]
        elif num_articles == max_articles:
            authors.append(author)
    authors.sort()
    return authors

def suggest_collaborators(id_to_article: ArxivType,
                          author: NameType) -> List[NameType]:
    """
    >>> suggest_collaborators(EXAMPLE_ARXIV, ('Pancer', 'Richard'))
    [('Ponce', 'Marcelo'), ('Tafliovich', 'Anya Y.')]
    >>> suggest_collaborators(EXAMPLE_ARXIV, ('Tafliovich', 'Anya Y.'))
    [('Pancer', 'Richard')]
    """
    collaborators = []
    coauthors = get_coauthors(id_to_article, author)
    for coauthor in coauthors:
        possible_collaborators = get_coauthors(id_to_article, coauthor)

        for collaborator in possible_collaborators:
            if collaborator != author and collaborator not in coauthors:
                collaborators.append(collaborator)

    return collaborators


def has_prolific_authors(author_to_articles: Dict[NameType, List[str]],
                         article: ArticleType, 
                         min_publications: int) -> bool:
    """
    >>> has_prolific_authors(EXAMPLE_BY_AUTHOR, EXAMPLE_ARXIV['008'], 2)
    True
    >>> has_prolific_authors(EXAMPLE_BY_AUTHOR, EXAMPLE_ARXIV['031'], 2)
    False
    """
    prolific_authors = []
    for author in author_to_articles:
        if  len(author_to_articles[author]) >= min_publications:
            prolific_authors.append(author)
    
    for author in article[AUTHORS]:
        if author in prolific_authors:
            return True
    return False



# We provide this PARTIAL docstring to show use of copy.deepcopy.
def keep_prolific_authors(id_to_article: ArxivType,
                          min_publications: int) -> None:
    """Update id_to_article so that it contains only articles published by
    authors with min_publications or more articles published. As long
    as at least one of the authors has min_publications, the article
    is kept.

    >>> arxiv_copy = copy.deepcopy(EXAMPLE_ARXIV)
    >>> keep_prolific_authors(arxiv_copy, 2)
    >>> len(arxiv_copy)
    3
    >>> '008' in arxiv_copy and '067' in arxiv_copy and '827' in arxiv_copy
    True
    """
    author_to_articles = make_author_to_articles(id_to_article)
    copy = id_to_article.copy()
    for _id in copy:
        article = id_to_article[_id]
        if not has_prolific_authors(author_to_articles, article, min_publications):
            id_to_article.pop(_id)
    


# Note that we do not include example calls since the function works
# on an input file.

def read_arxiv_file(afile: TextIO) -> ArxivType:
    """Return a dict containing all arxiv information in afile.

    Precondition: afile is open for reading
                  afile is in the format described in the handout
    """
    id_to_article = {}
    line = afile.readline()
    while line != '':
        article = {}
        article[ID] = line.strip()
        article[TITLE] = afile.readline().strip()
        article[CREATED]  = afile.readline().strip()
        article[MODIFIED]  = afile.readline().strip()

        authors = []
        
        line = afile.readline()
        while line != '\n':
            last, first = line.strip().split(',')
            authors.append((last, first))
            line = afile.readline()
        authors.sort()
        article[AUTHORS] = authors

        abstract = ''
        line = afile.readline()
        while line != 'END\n':
            abstract += line
            line = afile.readline()
        article[ABSTRACT] = abstract.strip()

        # clear
        for k in article:
            if article[k] == '':
                article[k] = None
        
        id_to_article[article[ID]] = article
        line = afile.readline()
    return id_to_article




    


if __name__ == '__main__':

    import doctest
    doctest.testmod()

    with open('example_data.txt') as example_data:
        example_arxiv = read_arxiv_file(example_data)
        print('Did we produce a correct dict? ',
              example_arxiv == EXAMPLE_ARXIV)

        # import pprint
        # pp = pprint.PrettyPrinter(indent=1)
        # pp.pprint(example_arxiv)

    # uncomment to work with a larger data set
    # with open('data.txt') as data:
    #    arxiv = read_arxiv_file(data)

    # author_to_articles = make_author_to_articles(arxiv)
    # most_published = get_most_published_authors(arxiv)
    # print(most_published)
    # print(get_coauthors(arxiv, ('Varanasi', 'Mahesh K.')))  # one
    # print(get_coauthors(arxiv, ('Chablat', 'Damien')))  # many
