"""Homework"""
def sites_on_date(visits: list, date: str)-> set[str]:
    """
    Returns set of all urls that have been visited
    on current date
    :param visits: all visits in the browser history
    (you get it as the result of the fucntion get_chrome_os
    from get_browser_history module)
    :param date: date in format "yyyy-mm-dd"
    :return: set of url visited on date

    >>> sites_on_date([
    ...     ('https://www.instagram.com/direct/t/114425786620592/', 'Чати • Instagram', \
'2024-08-06', '21:11:00.289043', 13198118),
    ...     ('https://www.instagram.com/direct/t/100421648030443/', '(2) Вхідні • Чати', \
'2024-08-06', '21:11:13.477121', 27761061),
    ...     ('https://www.instagram.com/stories/direct/3428527130146843066_1226238796', \
'Розповіді • Instagram', '2024-08-05', '21:11:14.988522', 253315)
    ... ], '2024-08-06') == {'https://www.instagram.com/direct/t/114425786620592/', \
'https://www.instagram.com/direct/t/100421648030443/'}
    True
    """
    output = set()
    for site in visits:
        if site[2] == date:
            output.add(site[0])
    return output

def most_frequent_sites(visits: list, number: int)-> set[str]:
    """
    Returns set of most frequent sites visited in total
    Return only 'number' of most frequent sites visited
    If the frequence is the same choose sites in the alphabetical order
    :param visits: all visits in browser history
    :param number: number of most frequent sites to return
    :return: set of most frequent sites
    >>> visits = [\
('https://www.instagram.com/direct/t/114425786620592/', 'Чати • Instagram', \
'2024-08-06', '21:11:00.289043', 13198118),\
('https://www.instagram.com/direct/t/100421648030443/', '(2) Вхідні • Чати', \
'2024-08-06', '21:11:13.477121', 27761061),\
('https://www.instagram.com/stories/direct/3428527130146843066_1226238796', \
'Розповіді • Instagram', '2024-08-06', '21:11:14.988522', 253315),\
('https://www.instagram.com/', 'Instagram', '2024-08-06', '21:11:41.236944', 3687575),\
        ]
    >>> most_frequent_sites(visits, 3) == {'https://www.instagram.com/direct/t/114425786620592/', \
'https://www.instagram.com/direct/t/100421648030443/', 'https://www.instagram.com/'}
    True
    """
    dict_of_visits = {}
    for site, *_ in visits:
        dict_of_visits[site] = dict_of_visits.get(site, 0) + 1

    list_of_sites = []
    for site, count in dict_of_visits.items():
        list_of_sites.append((count, site))

    lenght = len(list_of_sites)
    for i in range(lenght):
        for j in range(i + 1, lenght):
            if (list_of_sites[i][0] < list_of_sites[j][0]) or \
               (list_of_sites[i][0] == list_of_sites[j][0] and \
                list_of_sites[i][1] > list_of_sites[j][1]):
                list_of_sites[i], list_of_sites[j] = list_of_sites[j], list_of_sites[i]

    output = {site for _, site in list_of_sites[:number]}

    return output

def sort_date(tpl):
    """
    func is made as a key for sorting
    """
    return tpl[0], tpl[1]

def get_url_info(visits: list, url: str)->tuple:
    """
    Returns tuple with info about site, which title is passed
    Function should return:
    title - title of site with this url
    last_visit_date - date of the last visit of this site, in format "yyyy-mm-dd"
    last_visit_time - time of the last visit of this site, in format "hh:mm:ss.ms"
    num_of_visits - how much time was this site visited
    average_time - average time, spend on this site
    :param visits: all visits in browser history
    :param url: url of site to search
    :return: (title, last_visit_date, last_visit_time, num_of_visits, average_time)
    """
    count_visits = 0
    title, last_visit_date, last_visit_time = '', [], []
    all_times = []
    for site in visits:
        if site[0] == url:
            count_visits += 1
            title = site[1]
            last_visit_date.append(site[2])
            last_visit_time.append(site[3])
    if not title:
        return ('', '', '', 0, 0)

    last_visits = zip(last_visit_date, last_visit_time)
    last_visits = sorted(last_visits, key = sort_date)
    print(last_visits)
    for _, site in enumerate(visits):
        if site[0] == url:
            all_times.append(site[-1])
    all_times = sum(all_times)/len(all_times)
    return (title, last_visits[-1][0], last_visits[-1][1], count_visits, all_times)

if __name__ == '__main__':
    import doctest
    print(doctest.testmod())
