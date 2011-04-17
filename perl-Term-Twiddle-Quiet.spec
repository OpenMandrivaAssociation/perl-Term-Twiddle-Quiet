%define upstream_name    Term-Twiddle-Quiet
%define upstream_version 1.100110

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2

Summary:    Twiddles a thingy while-u-wait if run interactively
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Term/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(English)
BuildRequires: perl(File::Find)
BuildRequires: perl(IO::Interactive)
BuildRequires: perl(Module::Build)
BuildRequires: perl(Term::Twiddle)
BuildRequires: perl(Test::MockObject)
BuildRequires: perl(Test::More)
BuildRequires: perl(Module::Build)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
the Term::Twiddle manpage is a nice module for showing spinning thingies on
the terminal while waiting for an action to complete.

the Term::Twiddle::Quiet manpage acts very much like that module when it is
run interactively. However, when it isn't run interactively (for example,
as a cron job) then it does not show the twiddle.

Other than this difference, it really act as a the Term::Twiddle manpage
with all its options, methods and restrictions (of course, it supports the
same API) - cf its documentation for more information.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Build.PL installdirs=vendor

./Build

%check
./Build test

%install
rm -rf %buildroot
./Build install destdir=%{buildroot}

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes LICENSE README
%{_mandir}/man3/*
%perl_vendorlib/*


