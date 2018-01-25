%global srcname ldappool

Name:           python-%{srcname}
Version:        1.0
Release:        11%{?dist}
Url:            https://github.com/mozilla-services/ldappool
Summary:        A connection pool for python-ldap
License:        MPLv1.1 and GPLv2+ and LGPLv2+
Group:          Development/Libraries
Source:         http://pypi.python.org/packages/source/l/%{srcname}/%{srcname}-%{version}.tar.gz
BuildRequires:  python2-devel
BuildArch:      noarch

%global _description\
A simple connector pool for python-ldap.\
\
The pool keeps LDAP connectors alive and let you reuse them,\
drastically reducing the time spent to initiate a ldap connection.\
\
The pool has useful features like:\
\
- transparent re-connection on failures or server restarts\
- configurable pool size and connectors timeouts\
- configurable max lifetime for connectors\
- a context manager to simplify acquiring and releasing a connector

%description %_description

%package -n python2-%{srcname}
Summary: %summary
Requires:       python2-ldap
%{?python_provide:%python_provide python2-%{srcname}}

%description -n python2-%{srcname} %_description

%prep
%setup -q -n %{srcname}-%{version}

%build
python setup.py build

%install
python setup.py install --prefix=%{_prefix} --root=%{buildroot}

# FIXME: tests are not launched since they require an active LDAP server
# one could use nosetests to launch them

# FIXME: add license files as soon as upstream adds them
# https://github.com/mozilla-services/ldappool/issues/2

%files -n python2-%{srcname}
%doc README.rst
%{python_sitelib}/*

%changelog
* Thu Jan 25 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.0-11
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.0-10
- Python 2 binary package renamed to python2-ldappool
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-7
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 28 2012 Haïkel Guémar <hguemar@fedoraproject.org> - 1.0-0
- initial packaging

