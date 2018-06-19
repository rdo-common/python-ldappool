%global srcname ldappool

%if 0%{?rhel}
%global py2_prefix python
%bcond_with python3
%else
%global py2_prefix python2
%bcond_without python3
%endif


Name:           python-%{srcname}

Version:        2.1.0
Release:        3%{?dist}
Url:            https://github.com/mozilla-services/ldappool
Summary:        A connection pool for python-ldap
License:        MPLv1.1 and GPLv2+ and LGPLv2+
Source:         https://files.pythonhosted.org/packages/source/l/%{srcname}/%{srcname}-%{version}.tar.gz
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
Requires:       %{py2_prefix}-ldap
BuildRequires:  %{py2_prefix}-devel
BuildRequires:  %{py2_prefix}-setuptools
BuildRequires:  %{py2_prefix}-ldap
BuildRequires:  %{py2_prefix}-pbr
BuildRequires:  %{py2_prefix}-testtools
BuildRequires:  %{py2_prefix}-testresources
BuildRequires:  %{py2_prefix}-testrepository
%{?python_provide:%python_provide python2-%{srcname}}

%description -n python2-%{srcname} %_description

%if %{with python3}
%package -n python3-%{srcname}
Summary: %summary
Requires:       python3-pyldap
BuildRequires:  python3-devel
BuildRequires:  python3-pyldap
BuildRequires:  python3-pbr
BuildRequires:  python3-testtools
BuildRequires:  python3-testresources
BuildRequires:  python3-testrepository
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname} %_description
%endif

%prep
%setup -q -n %{srcname}-%{version}

%build
%py2_build
%if %{with python3}
%py3_build
%endif

%install
%py2_install
%if %{with python3}
%py3_install
%endif

%check
%if %{with python3}
%{__python3} setup.py testr
%endif
%{__python2} setup.py testr

# FIXME: add license files as soon as upstream adds them
# https://github.com/mozilla-services/ldappool/issues/2

%files -n python2-%{srcname}
%doc README.rst
%{python2_sitelib}/%{srcname}
%{python2_sitelib}/%{srcname}-%{version}-py?.?.egg-info

%if %{with python3}
%files -n python3-%{srcname}
%doc README.rst
%{python3_sitelib}/%{srcname}
%{python3_sitelib}/%{srcname}-%{version}-py?.?.egg-info
%endif


%changelog
* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.1.0-3
- Rebuilt for Python 3.7

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.1.0-2
- Rebuilt for Python 3.7

* Fri Apr 13 2018 Iryna Shcherbina <ishcherb@redhat.com> - 2.1.0-1
- Update to version 2.1.0 and run tests
- Add a Python 3 subpackage
- Add dependency on python-setuptools

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

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

