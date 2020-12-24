import { createSelector } from "@reduxjs/toolkit";
import { embassyAttributeIdx } from "../utils/USEmbassy";

// basic selectors
const metadataSelector = state => state.metadata;
const overviewSelector = state => state.visastatusOverview;
const newestSelector = state => state.visastatusNewest;
const filterSelector = state => state.visastatusFilter;
const embassyLstSelector = createSelector(metadataSelector, metadata => metadata.embassyLst);
export const makeEmbassyBySysSelector = sys =>
    createSelector(embassyLstSelector, embassyLst =>
        sys === "all"
            ? embassyLst.map(emb => emb[embassyAttributeIdx.code])
            : embassyLst.filter(emb => emb[embassyAttributeIdx.sys] === sys).map(emb => emb[embassyAttributeIdx.code]),
    );
const embassyOptionsSelector = createSelector(embassyLstSelector, embassyLst =>
    embassyLst.map(emb => ({ name: emb[embassyAttributeIdx.nameEn], code: emb[embassyAttributeIdx.code] })),
);
const rceTreeSelector = createSelector(metadataSelector, metadata => metadata.regionCountryEmbassyTree);
export const makeEmbassyTreeSelector = (sys, t) =>
    createSelector(
        [embassyOptionsSelector, rceTreeSelector, makeEmbassyBySysSelector(sys)],
        (embassyOptions, rceTree, embassyBySys) =>
            rceTree
                .map(({ region, countryEmbassyMap }) => ({
                    title: t(region),
                    value: region,
                    key: region,
                    children: countryEmbassyMap
                        .map(({ country, embassyCodeLst }) => ({
                            title: t(country),
                            value: country,
                            key: country,
                            children: embassyOptions
                                .filter(({ code }) => embassyCodeLst.includes(code) && embassyBySys.includes(code))
                                .map(({ code }) => ({ title: t(code), value: code, key: code })),
                        }))
                        .filter(countryNode => countryNode.children.length > 0),
                }))
                .filter(regionNode => regionNode.children.length > 0),
    );

// generate `make{Some}SelectorByVisaType`
const makeSelectorMakerByVisaType = selector => visType => createSelector(selector, output => output[visType]);

// Selectors by Visa type
const makeOverviewSelectorByVisaType = makeSelectorMakerByVisaType(overviewSelector);
export const makeFilterSelectorByVisaType = makeSelectorMakerByVisaType(filterSelector);

export const makeOverviewDetailSelector = visaType =>
    createSelector(
        [makeOverviewSelectorByVisaType(visaType), makeFilterSelectorByVisaType(visaType)],
        (overview, filter) =>
            filter.map(
                code =>
                    overview.find(ov => ov.embassyCode === code) || {
                        visaType,
                        embassyCode: code,
                        earliestDate: ["/"],
                        latestDate: ["/"],
                    },
            ),
    );

export const makeNewestVisaStatusSelector = (visaType, embassyCode) =>
    createSelector(newestSelector, newest => newest[visaType][embassyCode]);
